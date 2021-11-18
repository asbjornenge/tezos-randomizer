###
#
# Added from elsewhere, needs work.
#
###

  @sp.entry_point(private = True)
  def verifyShuffle(self):
    shuffledValues = sp.local('shuffledValues', sp.set([]))
    sp.for v in self.data.shuffled.values():
      shuffledValues.value.add(v)
    sp.verify_equal(sp.len(self.data.shuffled.values()), sp.len(shuffledValues.value))

  @sp.entry_point
  def shuffle(self):
    self.checkAdmin()
    shuffled = sp.local('shuffled', {})
    index = sp.local('index', 0)
    remaining = sp.local('remaining', sp.set([]))
    _selected = sp.local('_selected', 0)

    sp.while index.value < self.data.totalSupply:
      remaining.value.add(index.value)
      index.value += 1
    
    index.value = 0
    ent = sp.pack(sp.now)
    sp.while sp.len(remaining.value) > 0: 
      _len = sp.len(remaining.value)
      nat = self.hash_to_nat(ent + sp.pack(_len) + sp.pack(self.data.randomStartIndex))
      rnd = nat % _len
      sp.if remaining.value.contains(rnd) == False:
        sp.for rem in remaining.value.elements():
          _selected.value = rem
        shuffled.value[index.value] = _selected.value
        remaining.value.remove(_selected.value)
        index.value += 1
      sp.else:
        shuffled.value[index.value] = rnd
        remaining.value.remove(rnd)
        index.value += 1
    #sp.trace(shuffled.value.keys())
    #sp.trace(shuffled.value.values())
    self.data.shuffled = shuffled.value
    self.data.isShuffled = True

@sp.add_target(name="Shuffle", kind=allTarget)
def test():
  scenario = sp.test_scenario()
  admin = sp.address("tz1-admin")
  user1 = sp.address("tz1-user-1")
  user2 = sp.address("tz1-user-2")
  totalSupply = 11
  maxPerWallet = 6
  mintStartIndex = 0
  cost = 10
  startTime = int(datetime.now().timestamp())
  whitelistStartTime = startTime
  reserveAmount = 0
  minter, token = initMinter(admin, scenario, cost, totalSupply, maxPerWallet, {
    user1: 100
  }, startTime, whitelistStartTime, reserveAmount)
  mint(token, admin, minter.address, scenario, mintStartIndex, totalSupply)

  scenario += minter.shuffle().run(sender=admin)
  scenario.verify(sp.len(minter.data.shuffled) == totalSupply)
  scenario += minter.verifyShuffle()

  scenario += minter.mint(5).run(sender=user1, amount=sp.tez(50), now=sp.timestamp(startTime+1))
  scenario += minter.mint(6).run(sender=user2, amount=sp.tez(60), now=sp.timestamp(startTime+1))
  scenario.verify(minter.data.minted == 11)
