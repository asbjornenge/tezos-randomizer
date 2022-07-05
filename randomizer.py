import smartpy as sp
        
class Randomizer(sp.Contract):
  def __init__(self, admin, metadata):
    self.init(
      admins=sp.set([admin]),
      metadata=metadata,
      entropy=sp.bytes('0x'),
      bytes_to_nat = {
        sp.bytes('0x00'): 0, sp.bytes('0x01'): 1,
        sp.bytes('0x02'): 2, sp.bytes('0x03'): 3,
        sp.bytes('0x04'): 4, sp.bytes('0x05'): 5,
        sp.bytes('0x06'): 6, sp.bytes('0x07'): 7,
        sp.bytes('0x08'): 8, sp.bytes('0x09'): 9,
        sp.bytes('0x0a'): 10, sp.bytes('0x0b'): 11,
        sp.bytes('0x0c'): 12, sp.bytes('0x0d'): 13,
        sp.bytes('0x0e'): 14, sp.bytes('0x0f'): 15,
        sp.bytes('0x10'): 16, sp.bytes('0x11'): 17,
        sp.bytes('0x12'): 18, sp.bytes('0x13'): 19,
        sp.bytes('0x14'): 20, sp.bytes('0x15'): 21,
        sp.bytes('0x16'): 22, sp.bytes('0x17'): 23,
        sp.bytes('0x18'): 24, sp.bytes('0x19'): 25,
        sp.bytes('0x1a'): 26, sp.bytes('0x1b'): 27,
        sp.bytes('0x1c'): 28, sp.bytes('0x1d'): 29,
        sp.bytes('0x1e'): 30, sp.bytes('0x1f'): 31,
        sp.bytes('0x20'): 32, sp.bytes('0x21'): 33,
        sp.bytes('0x22'): 34, sp.bytes('0x23'): 35,
        sp.bytes('0x24'): 36, sp.bytes('0x25'): 37,
        sp.bytes('0x26'): 38, sp.bytes('0x27'): 39,
        sp.bytes('0x28'): 40, sp.bytes('0x29'): 41,
        sp.bytes('0x2a'): 42, sp.bytes('0x2b'): 43,
        sp.bytes('0x2c'): 44, sp.bytes('0x2d'): 45,
        sp.bytes('0x2e'): 46, sp.bytes('0x2f'): 47,
        sp.bytes('0x30'): 48, sp.bytes('0x31'): 49,
        sp.bytes('0x32'): 50, sp.bytes('0x33'): 51,
        sp.bytes('0x34'): 52, sp.bytes('0x35'): 53,
        sp.bytes('0x36'): 54, sp.bytes('0x37'): 55,
        sp.bytes('0x38'): 56, sp.bytes('0x39'): 57,
        sp.bytes('0x3a'): 58, sp.bytes('0x3b'): 59,
        sp.bytes('0x3c'): 60, sp.bytes('0x3d'): 61,
        sp.bytes('0x3e'): 62, sp.bytes('0x3f'): 63,
        sp.bytes('0x40'): 64, sp.bytes('0x41'): 65,
        sp.bytes('0x42'): 66, sp.bytes('0x43'): 67,
        sp.bytes('0x44'): 68, sp.bytes('0x45'): 69,
        sp.bytes('0x46'): 70, sp.bytes('0x47'): 71,
        sp.bytes('0x48'): 72, sp.bytes('0x49'): 73,
        sp.bytes('0x4a'): 74, sp.bytes('0x4b'): 75,
        sp.bytes('0x4c'): 76, sp.bytes('0x4d'): 77,
        sp.bytes('0x4e'): 78, sp.bytes('0x4f'): 79,
        sp.bytes('0x50'): 80, sp.bytes('0x51'): 81,
        sp.bytes('0x52'): 82, sp.bytes('0x53'): 83,
        sp.bytes('0x54'): 84, sp.bytes('0x55'): 85,
        sp.bytes('0x56'): 86, sp.bytes('0x57'): 87,
        sp.bytes('0x58'): 88, sp.bytes('0x59'): 89,
        sp.bytes('0x5a'): 90, sp.bytes('0x5b'): 91,
        sp.bytes('0x5c'): 92, sp.bytes('0x5d'): 93,
        sp.bytes('0x5e'): 94, sp.bytes('0x5f'): 95,
        sp.bytes('0x60'): 96, sp.bytes('0x61'): 97,
        sp.bytes('0x62'): 98, sp.bytes('0x63'): 99,
        sp.bytes('0x64'): 100, sp.bytes('0x65'): 101,
        sp.bytes('0x66'): 102, sp.bytes('0x67'): 103,
        sp.bytes('0x68'): 104, sp.bytes('0x69'): 105,
        sp.bytes('0x6a'): 106, sp.bytes('0x6b'): 107,
        sp.bytes('0x6c'): 108, sp.bytes('0x6d'): 109,
        sp.bytes('0x6e'): 110, sp.bytes('0x6f'): 111,
        sp.bytes('0x70'): 112, sp.bytes('0x71'): 113,
        sp.bytes('0x72'): 114, sp.bytes('0x73'): 115,
        sp.bytes('0x74'): 116, sp.bytes('0x75'): 117,
        sp.bytes('0x76'): 118, sp.bytes('0x77'): 119,
        sp.bytes('0x78'): 120, sp.bytes('0x79'): 121,
        sp.bytes('0x7a'): 122, sp.bytes('0x7b'): 123,
        sp.bytes('0x7c'): 124, sp.bytes('0x7d'): 125,
        sp.bytes('0x7e'): 126, sp.bytes('0x7f'): 127,
        sp.bytes('0x80'): 128, sp.bytes('0x81'): 129,
        sp.bytes('0x82'): 130, sp.bytes('0x83'): 131,
        sp.bytes('0x84'): 132, sp.bytes('0x85'): 133,
        sp.bytes('0x86'): 134, sp.bytes('0x87'): 135,
        sp.bytes('0x88'): 136, sp.bytes('0x89'): 137,
        sp.bytes('0x8a'): 138, sp.bytes('0x8b'): 139,
        sp.bytes('0x8c'): 140, sp.bytes('0x8d'): 141,
        sp.bytes('0x8e'): 142, sp.bytes('0x8f'): 143,
        sp.bytes('0x90'): 144, sp.bytes('0x91'): 145,
        sp.bytes('0x92'): 146, sp.bytes('0x93'): 147,
        sp.bytes('0x94'): 148, sp.bytes('0x95'): 149,
        sp.bytes('0x96'): 150, sp.bytes('0x97'): 151,
        sp.bytes('0x98'): 152, sp.bytes('0x99'): 153,
        sp.bytes('0x9a'): 154, sp.bytes('0x9b'): 155,
        sp.bytes('0x9c'): 156, sp.bytes('0x9d'): 157,
        sp.bytes('0x9e'): 158, sp.bytes('0x9f'): 159,
        sp.bytes('0xa0'): 160, sp.bytes('0xa1'): 161,
        sp.bytes('0xa2'): 162, sp.bytes('0xa3'): 163,
        sp.bytes('0xa4'): 164, sp.bytes('0xa5'): 165,
        sp.bytes('0xa6'): 166, sp.bytes('0xa7'): 167,
        sp.bytes('0xa8'): 168, sp.bytes('0xa9'): 169,
        sp.bytes('0xaa'): 170, sp.bytes('0xab'): 171,
        sp.bytes('0xac'): 172, sp.bytes('0xad'): 173,
        sp.bytes('0xae'): 174, sp.bytes('0xaf'): 175,
        sp.bytes('0xb0'): 176, sp.bytes('0xb1'): 177,
        sp.bytes('0xb2'): 178, sp.bytes('0xb3'): 179,
        sp.bytes('0xb4'): 180, sp.bytes('0xb5'): 181,
        sp.bytes('0xb6'): 182, sp.bytes('0xb7'): 183,
        sp.bytes('0xb8'): 184, sp.bytes('0xb9'): 185,
        sp.bytes('0xba'): 186, sp.bytes('0xbb'): 187,
        sp.bytes('0xbc'): 188, sp.bytes('0xbd'): 189,
        sp.bytes('0xbe'): 190, sp.bytes('0xbf'): 191,
        sp.bytes('0xc0'): 192, sp.bytes('0xc1'): 193,
        sp.bytes('0xc2'): 194, sp.bytes('0xc3'): 195,
        sp.bytes('0xc4'): 196, sp.bytes('0xc5'): 197,
        sp.bytes('0xc6'): 198, sp.bytes('0xc7'): 199,
        sp.bytes('0xc8'): 200, sp.bytes('0xc9'): 201,
        sp.bytes('0xca'): 202, sp.bytes('0xcb'): 203,
        sp.bytes('0xcc'): 204, sp.bytes('0xcd'): 205,
        sp.bytes('0xce'): 206, sp.bytes('0xcf'): 207,
        sp.bytes('0xd0'): 208, sp.bytes('0xd1'): 209,
        sp.bytes('0xd2'): 210, sp.bytes('0xd3'): 211,
        sp.bytes('0xd4'): 212, sp.bytes('0xd5'): 213,
        sp.bytes('0xd6'): 214, sp.bytes('0xd7'): 215,
        sp.bytes('0xd8'): 216, sp.bytes('0xd9'): 217,
        sp.bytes('0xda'): 218, sp.bytes('0xdb'): 219,
        sp.bytes('0xdc'): 220, sp.bytes('0xdd'): 221,
        sp.bytes('0xde'): 222, sp.bytes('0xdf'): 223,
        sp.bytes('0xe0'): 224, sp.bytes('0xe1'): 225,
        sp.bytes('0xe2'): 226, sp.bytes('0xe3'): 227,
        sp.bytes('0xe4'): 228, sp.bytes('0xe5'): 229,
        sp.bytes('0xe6'): 230, sp.bytes('0xe7'): 231,
        sp.bytes('0xe8'): 232, sp.bytes('0xe9'): 233,
        sp.bytes('0xea'): 234, sp.bytes('0xeb'): 235,
        sp.bytes('0xec'): 236, sp.bytes('0xed'): 237,
        sp.bytes('0xee'): 238, sp.bytes('0xef'): 239,
        sp.bytes('0xf0'): 240, sp.bytes('0xf1'): 241,
        sp.bytes('0xf2'): 242, sp.bytes('0xf3'): 243,
        sp.bytes('0xf4'): 244, sp.bytes('0xf5'): 245,
        sp.bytes('0xf6'): 246, sp.bytes('0xf7'): 247,
        sp.bytes('0xf8'): 248, sp.bytes('0xf9'): 249,
        sp.bytes('0xfa'): 250, sp.bytes('0xfb'): 251,
        sp.bytes('0xfc'): 252, sp.bytes('0xfd'): 253,
        sp.bytes('0xfe'): 254, sp.bytes('0xff'): 255
      }
    )

  ## Helper functions
  #

  def _get_discrete_random_number(self, n, entropy_in):
      # generate a non-biased uniform random discrete number between 0 and n
      # by using a combination of rejection sampling and modulo reduction

      multiplier = 256 / n

      entropy = sp.local('entropy', entropy_in)
      hash_len = sp.local("hash_len", sp.len(entropy_in))
      x = sp.local('x', 0)
      found = sp.local('found', False)
      result = sp.local('result', 0)
      with sp.while_(~found.value):
          with sp.while_((x.value < hash_len.value) &(~found.value)):
              result.value = self.data.bytes_to_nat[sp.slice(entropy.value, x.value, 1).open_some()]
              with sp.if_(result.value < multiplier*n):
                  found.value = True
              x.value += 1
          with sp.if_(~found.value):
              # statistically almost impossible to occcur
              x.value = 0
              entropy.value = sp.sha256(entropy.value)
      return result.value % n

  ## Verifiers
  #

  def checkAdmin(self):
    sp.verify(self.data.admins.contains(sp.sender), 'Only admin can call this entrypoint')

  ## Admin entrypoints
  #

  @sp.entry_point
  def addAdmin(self, admin):
    self.checkAdmin()
    self.data.admins.add(admin) 

  @sp.entry_point
  def delAdmin(self, admin):
    self.checkAdmin()
    self.data.admins.remove(admin) 

  @sp.entry_point
  def setEntropy(self, entropy):
    sp.set_type(entropy, sp.TNat)
    self.checkAdmin()
    self.data.entropy = sp.sha256(sp.pack(entropy))

  ## GetRandomNumber Callback Entrypoints
  #

  @sp.entry_point
  def getRBC(self, _from, _to, callback_address):
    res = self._get_discrete_random_number(sp.as_nat(_to - _from), sp.sha256(sp.pack(sp.now) + self.data.entropy)) + _from
    c = sp.contract(sp.TNat, callback_address).open_some()
    sp.transfer(res, sp.mutez(0), c)

  @sp.entry_point
  def getRBCE(self, _from, _to, entropy, callback_address):
    sp.set_type(entropy, sp.TNat)
    res = self._get_discrete_random_number(sp.as_nat(_to-_from), sp.sha256(sp.pack(entropy))) + _from
    c = sp.contract(sp.TNat, callback_address).open_some()
    sp.transfer(res, sp.mutez(0), c)

  @sp.entry_point
  def getRBCEB(self, _from, _to, entropy, includeRandomizerEntropy, callback_address):
    sp.set_type(entropy, sp.TBytes)
    sp.set_type(includeRandomizerEntropy, sp.TBool)
    _entropy = sp.local('_entropy', entropy)
    sp.if includeRandomizerEntropy:
      _entropy.value = _entropy.value + self.data.entropy
    res = self._get_discrete_random_number(sp.as_nat(_to-_from), sp.sha256(_entropy.value)) + _from
    c = sp.contract(sp.TNat, callback_address).open_some()
    sp.transfer(res, sp.mutez(0), c)

  ## GetRandomNumber onChain Views
  #

  @sp.onchain_view()
  def getRandomBetween(self, params):

    res = self._get_discrete_random_number(sp.as_nat(params._to-params._from), sp.sha256(sp.pack(sp.now)+self.data.entropy)) + params._from
    sp.result(res)

  @sp.onchain_view()
  def getRandomBetweenEntropy(self, params):
    sp.set_type(params.entropy, sp.TNat)
    res = self._get_discrete_random_number(sp.as_nat(params._to-params._from), sp.sha256(sp.pack(params.entropy))) + params._from
    sp.result(res)

  @sp.onchain_view()
  def getRandomBetweenEntropyBytes(self, params):
    sp.set_type(params.entropy, sp.TBytes)
    sp.set_type(params.includeRandomizerEntropy, sp.TBool)
    _entropy = sp.local('_entropy', params.entropy)
    sp.if params.includeRandomizerEntropy:
      _entropy.value = _entropy.value + self.data.entropy
    res = self._get_discrete_random_number(sp.as_nat(params._to-params._from), sp.sha256(_entropy.value)) + params._from
    sp.result(res)
