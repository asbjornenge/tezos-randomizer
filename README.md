# Tezos Randomizer

Tezos Randomizer is a contract that you can call from your own contracts to get a random number between X and Y - on-chain :chains:. 
It comes with a [service](https://github.com/asbjornenge/tezos-randomizer-service) that can be used to generate new entropy every X minutes (currently every 30 minutes for mainnet).
It also has `entrypoints` and `views` where you can "bring your own entropy".

If you use this software, donate :point_right: tz1UZZnrre9H7KzAufFVm7ubuJh5cCfjGwam

## Contracts

### v3

* Mainnet
  * [KT1UcszCkuL5eMpErhWxpRmuniAecD227Dwp](https://better-call.dev/mainnet/KT1UcszCkuL5eMpErhWxpRmuniAecD227Dwp/)
* Ghostnet 
  * [KT1Ls4XzMgz59Z2UxRroAtrQ8gN8c5AWeV9B](https://better-call.dev/ghostnet/KT1Ls4XzMgz59Z2UxRroAtrQ8gN8c5AWeV9B/)
* Ithacanet 
  * [KT1Ls4XzMgz59Z2UxRroAtrQ8gN8c5AWeV9B](https://better-call.dev/ithacanet/KT1Ls4XzMgz59Z2UxRroAtrQ8gN8c5AWeV9B/)
* Hangzhounet
  * [KT19etCHSt75MTF4NvUHxRNBPvp74ggv9g3P](https://better-call.dev/hangzhou2net/KT19etCHSt75MTF4NvUHxRNBPvp74ggv9g3P/)

### v2

* Mainnet
  * [KT1AAQzoUGFQ4HRg4qrYKY925ekNxavb7pkj](https://better-call.dev/mainnet/KT1AAQzoUGFQ4HRg4qrYKY925ekNxavb7pkj/)
* Hangzhounet
  * [KT1F3yK7z7AsYvLdHwiJmFnM8thtTHeuZWTf](https://better-call.dev/hangzhou2net/KT1F3yK7z7AsYvLdHwiJmFnM8thtTHeuZWTf/)
* Granadanet
  * [KT18nMUHUjAHmJBYR2kSFASCCp9e4xzCNKzk](https://better-call.dev/granadanet/KT18nMUHUjAHmJBYR2kSFASCCp9e4xzCNKzk/)

## Import

```
# v3.0.0
Randomizer = sp.io.import_script_from_url("https://ipfs.infura.io/ipfs/QmPNkabMCpDmFE6GynfS9UAoQDLE6PyCLpRJQmceEp2oTv")
# v2.0.0
Randomizer = sp.io.import_script_from_url("https://ipfs.infura.io/ipfs/QmWMFUneMRphK1uGKZaYjRXo8eJxRxB9rLU453DHrrBE1w")
# v1.0.0
Randomizer = sp.io.import_script_from_url("https://ipfs.infura.io/ipfs/QmeQ8QUmbQ1oV9FQb65UxgbM5323yuKNFgk3WgTzgzeY3E")
```

## Setup environment

```
./scipts/init-env.sh
source bin/activate
```

## Test

```
spy kind all tests.py output --html
```


## Compile & Deploy

```
spy compile compile.py compiled
spy originate-contract --code compiled/randomizer/step_000_cont_0_contract.tz --storage compiled/randomizer/step_000_cont_0_storage.json --rpc https://hangzhounet.smartpy.io
```

## Views

```
getRandomBetween
  parameters:
    _from: TNat
    _to: TNat

  Get a random number between _from and _to using storage entropy. 
    
getRandomBetweenEntropy
  parameters:
    _from: TNat
    _to: TNat
    entropy: TNat

  Get a random number between _from and _to using passed entropy (Nat).

getRandomBetweenEntropyBytes
  parameters:
    _from: TNat
    _to: TNat
    entropy: TBytes
    includeRandomizerEntropy: TBool

  Get a random number between _from and _to using passed entropy (Bytes).
  Concatenate passed entropy with randomizer entropy by passing includeRandomizerEntropy=True.
```

## Entrypoints

```
getRBC
  parameters:
    _from: TNat
    _to: TNat
    callback_address: TAddress

  Get a random number between _from and _to using storage entropy. 
  Does a callback with the result to `callback_address`.

getRBCE
  parameters:
    _from: TNat
    _to: TNat
    entropy: TNat
    callback_address: TAddress

  Get a random number between _from and _to using passed entropy.
  Does a callback with the result to `callback_address`.

getRBCEB
  parameters:
    _from: TNat
    _to: TNat
    entropy: TBytes
    includeRandomizerEntropy: TBool
    callback_address: TAddress

  Get a random number between _from and _to using passed entropy.
  Concatenate passed entropy with randomizer entropy by passing includeRandomizerEntropy=True.
  Does a callback with the result to `callback_address`.
```


## TODO

* Look into rejection sampling
* Entrypoint to get multiple values (unique / non-unique optionally)

enjoy. 
