import smartpy as sp
from datetime import datetime

Randomizer = sp.io.import_script_from_url("file:randomizer.py")
Harbinger = sp.io.import_script_from_url("file:///Users/asbjorn/srv/asbjornenge/harbinger-contracts/normalizer.py")

@sp.add_target(name="Randomizer", kind="randomizer")
def test():
  scenario = sp.test_scenario()

  ## Prepare Harbinger Oracle

  normalizer = Harbinger.NormalizerContract()
  scenario += normalizer 
  scenario += normalizer.update(
    Harbinger.makeMap(
      assetCode="XTZ-USD",
      start=sp.timestamp(1),
      end=sp.timestamp(2),
      open=1,
      high=2,
      low=3,
      close=4,
      volume=5
    )
  ).run(sender=Harbinger.defaultOracleContractAddress)

  ## Randomizer

  randomizer = Randomizer.Randomizer(
    normalizer.address, 
    "XTZ-USD",
    metadata = sp.big_map(
      {
        "": sp.utils.bytes_of_string("tezos-storage:content"),
        "content": sp.utils.bytes_of_string('{"name": "Randomizer"}')
      }
    )
  )
  scenario += randomizer
  scenario += randomizer.initHarbingerEntropy() 
  randomCaller = Randomizer.RandomCaller(randomizer.address)
  scenario += randomCaller 

  scenario += normalizer.update(
    Harbinger.makeMap(
      assetCode="XTZ-USD",
      start=sp.timestamp(3),
      end=sp.timestamp(4),
      open=1,
      high=10,
      low=5,
      close=6,
      volume=50
    )
  ).run(sender=Harbinger.defaultOracleContractAddress)

  scenario += randomCaller.getRandomNumber(sp.record(_from=5, _to=10)).run(now=sp.timestamp(int(datetime.now().timestamp())))
  scenario.verify(randomCaller.data.randomNumber >= 5)
  scenario.verify(randomCaller.data.randomNumber <= 10)

  scenario += normalizer.update(
    Harbinger.makeMap(
      assetCode="XTZ-USD",
      start=sp.timestamp(5),
      end=sp.timestamp(6),
      open=2,
      high=100,
      low=25,
      close=30,
      volume=500
    )
  ).run(sender=Harbinger.defaultOracleContractAddress)

  scenario += randomCaller.getRandomNumber(sp.record(_from=0, _to=7000)).run(now=sp.timestamp(int(datetime.now().timestamp())))
  scenario.verify(randomCaller.data.randomNumber >= 0)
  scenario.verify(randomCaller.data.randomNumber <= 7000)

  scenario += normalizer.update(
    Harbinger.makeMap(
      assetCode="XTZ-USD",
      start=sp.timestamp(6),
      end=sp.timestamp(7),
      open=30,
      high=30,
      low=4,
      close=5,
      volume=1000
    )
  ).run(sender=Harbinger.defaultOracleContractAddress)

  scenario += randomCaller.getRandomNumber(sp.record(_from=1111, _to=2222)).run(now=sp.timestamp(int(datetime.now().timestamp())))
  scenario.verify(randomCaller.data.randomNumber >= 1111)
  scenario.verify(randomCaller.data.randomNumber <= 2222)
