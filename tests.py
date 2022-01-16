import smartpy as sp
from datetime import datetime

Randomizer = sp.io.import_script_from_url("file:randomizer.py")
Caller = sp.io.import_script_from_url("file:caller.py")

allKind = 'all'

def initRandomizer(admin, scenario):
  randomizer = Randomizer.Randomizer(
    admin,
    metadata = sp.big_map(
      {
        "": sp.utils.bytes_of_string("tezos-storage:content"),
        "content": sp.utils.bytes_of_string('{"name": "Randomizer"}')
      }
    )
  )
  scenario += randomizer
  caller = Caller.RandomCaller(randomizer.address)
  scenario += caller
  return randomizer, caller

@sp.add_target(name="Admin", kind=allKind)
def test():
  admin = sp.address("tz1-admin")
  user1 = sp.address("tz1-user1")
  scenario = sp.test_scenario()
  randomizer, caller = initRandomizer(admin, scenario)

  ## Admin can set entropy

  scenario += randomizer.setEntropy(123456).run(sender=user1, valid=False, exception='Only admin can call this entrypoint') 
  scenario += randomizer.setEntropy(123456).run(sender=admin) 

  ## TODO: test setAdmin

@sp.add_target(name="Callback", kind=allKind)
def test():
  admin = sp.address("tz1-admin")
  user1 = sp.address("tz1-user1")
  scenario = sp.test_scenario()
  calltime = 1637752889 
  randomizer, caller = initRandomizer(admin, scenario)

  scenario += caller.getRandomNumber(sp.record(_from=5, _to=10)).run(now=sp.timestamp(calltime))
  scenario.verify(caller.data.randomNumber >= 5)
  scenario.verify(caller.data.randomNumber <= 10)
  scenario.verify(caller.data.randomNumber == 8)

  scenario += caller.getRandomNumber(sp.record(_from=5, _to=10)).run(now=sp.timestamp(calltime+1000))
  scenario.verify(caller.data.randomNumber >= 5)
  scenario.verify(caller.data.randomNumber <= 10)
  scenario.verify(caller.data.randomNumber == 6)

  scenario += caller.getRandomNumber(sp.record(_from=0, _to=7000)).run(now=sp.timestamp(int(datetime.now().timestamp())))
  scenario.verify(caller.data.randomNumber >= 0)
  scenario.verify(caller.data.randomNumber <= 7000)

  scenario += caller.getRandomNumber(sp.record(_from=1111, _to=2222)).run(now=sp.timestamp(int(datetime.now().timestamp())))
  scenario.verify(caller.data.randomNumber >= 1111)
  scenario.verify(caller.data.randomNumber <= 2222)

@sp.add_target(name="OnChainView", kind=allKind)
def test():
  admin = sp.address("tz1-admin")
  user1 = sp.address("tz1-user1")
  scenario = sp.test_scenario()
  calltime = 1637752889 
  randomizer, caller = initRandomizer(admin, scenario)

  scenario += randomizer.setEntropy(12345).run(sender=admin)
  scenario += caller.getRandomNumberSync(sp.record(_from=0,_to=100)).run(now=sp.timestamp(calltime))
  scenario.verify(caller.data.randomNumber == 11)
  scenario += randomizer.setEntropy(54321).run(sender=admin)
  scenario += caller.getRandomNumberSync(sp.record(_from=0,_to=100)).run(now=sp.timestamp(calltime))
  scenario.verify(caller.data.randomNumber == 42)

@sp.add_target(name="BringEntropy", kind=allKind)
def test():
  admin = sp.address("tz1-admin")
  user1 = sp.address("tz1-user1")
  scenario = sp.test_scenario()
  calltime = 1637752889 
  randomizer, caller = initRandomizer(admin, scenario)

  scenario += caller.getRandomNumberEntropy(sp.record(_from=0,_to=100,entropy=12345))
  scenario.verify(caller.data.randomNumber == 63)
  scenario += caller.getRandomNumberEntropy(sp.record(_from=0,_to=100,entropy=54321))
  scenario.verify(caller.data.randomNumber == 28)

  scenario += caller.getRandomNumberSyncEntropy(sp.record(_from=0,_to=100,entropy=12345))
  scenario.verify(caller.data.randomNumber == 63)
  scenario += caller.getRandomNumberSyncEntropy(sp.record(_from=0,_to=100,entropy=54321))
  scenario.verify(caller.data.randomNumber == 28)

@sp.add_target(name="BringEntropyBytes", kind=allKind)
def test():
  admin = sp.address("tz1-admin")
  user1 = sp.address("tz1-user1")
  scenario = sp.test_scenario()
  calltime = 1637752889 
  randomizer, caller = initRandomizer(admin, scenario)

  scenario += caller.getRandomNumberEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(12345), includeRandomizerEntropy=False))
  scenario.verify(caller.data.randomNumber == 63)
  scenario += caller.getRandomNumberEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(54321), includeRandomizerEntropy=False))
  scenario.verify(caller.data.randomNumber == 28)

  scenario += caller.getRandomNumberSyncEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(12345), includeRandomizerEntropy=False))
  scenario.verify(caller.data.randomNumber == 63)
  scenario += caller.getRandomNumberSyncEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(54321), includeRandomizerEntropy=False))
  scenario.verify(caller.data.randomNumber == 28)

  scenario += randomizer.setEntropy(12345).run(sender = admin)

  scenario += caller.getRandomNumberEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(12345), includeRandomizerEntropy=True))
  scenario.verify(caller.data.randomNumber == 89)
  scenario += caller.getRandomNumberEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(54321), includeRandomizerEntropy=True))
  scenario.verify(caller.data.randomNumber == 91)

  scenario += caller.getRandomNumberSyncEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(12345), includeRandomizerEntropy=True))
  scenario.verify(caller.data.randomNumber == 89)
  scenario += caller.getRandomNumberSyncEntropyBytes(sp.record(_from=0,_to=100,entropy=sp.pack(54321), includeRandomizerEntropy=True))
  scenario.verify(caller.data.randomNumber == 91)
