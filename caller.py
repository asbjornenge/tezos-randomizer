import smartpy as sp

class RandomCaller(sp.Contract):
  def __init__(self, randomizer):
    self.init(
      randomNumber=0,
      randomizer=randomizer
    )

  @sp.entry_point
  def setRandomNumber(self, randomNumber):
    sp.set_type(randomNumber, sp.TNat)
    sp.if sp.sender != self.data.randomizer:
      sp.failwith('Only Randomizer can call this entrypoint')
    self.data.randomNumber = randomNumber

  @sp.entry_point
  def getRandomNumber(self, _from, _to):
    callback_address = sp.self_entry_point_address(entry_point = 'setRandomNumber')
    c = sp.contract(sp.TRecord(_from=sp.TNat, _to=sp.TNat, callback_address=sp.TAddress), self.data.randomizer, entry_point="getRandomBetweenCallback").open_some()
    sp.transfer(sp.record(_from=_from, _to=_to, callback_address=callback_address), sp.mutez(0), c)

  @sp.entry_point
  def getRandomNumberEntropy(self, _from, _to, entropy):
    callback_address = sp.self_entry_point_address(entry_point = 'setRandomNumber')
    c = sp.contract(sp.TRecord(_from=sp.TNat, _to=sp.TNat, entropy=sp.TNat, callback_address=sp.TAddress), self.data.randomizer, entry_point="getRandomBetweenCallbackEntropy").open_some()
    sp.transfer(sp.record(_from=_from, _to=_to, entropy=entropy, callback_address=callback_address), sp.mutez(0), c)
 
  @sp.entry_point
  def getRandomNumberSync(self, _from, _to):
    arg =  sp.record(_from = _from, _to = _to)
    rnum = sp.view("getRandomBetween", self.data.randomizer, arg, sp.TNat).open_some("Invalid view");
    self.data.randomNumber = rnum
    sp.verify(rnum >= _from, "Value is to low")
    sp.verify(rnum <= _to, "Value is to high")

  @sp.entry_point
  def getRandomNumberSyncEntropy(self, _from, _to, entropy):
    arg =  sp.record(_from=_from, _to=_to, entropy=entropy)
    rnum = sp.view("getRandomBetweenEntropy", self.data.randomizer, arg, sp.TNat).open_some("Invalid view");
    self.data.randomNumber = rnum
    sp.verify(rnum >= _from, "Value is to low")
    sp.verify(rnum <= _to, "Value is to high")
