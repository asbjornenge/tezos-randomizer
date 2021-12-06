# Tezos Randomizer

Tezos Randomizer is a contract that you can call from your own contracts to get a random number between X and Y - on-chain :chains:. 
It comes with a [service](https://github.com/asbjornenge/tezos-randomizer-service) that can be used to generate new entropy every X minutes (currently every 30 minutes for mainnet).
It also has `entrypoints` and `views` where you can "bring your own entropy".

If you use this software, donate :point_right: tz1UZZnrre9H7KzAufFVm7ubuJh5cCfjGwam

## Contracts

* Mainnet
  * [KT1AAQzoUGFQ4HRg4qrYKY925ekNxavb7pkj](https://better-call.dev/mainnet/KT1AAQzoUGFQ4HRg4qrYKY925ekNxavb7pkj/)
* Granadanet
  * [KT18nMUHUjAHmJBYR2kSFASCCp9e4xzCNKzk](https://better-call.dev/granadanet/KT18nMUHUjAHmJBYR2kSFASCCp9e4xzCNKzk/)

## Import

```
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
spy originate-contract --code compiled/randomizer/step_000_cont_0_contract.tz --storage compiled/randomizer/step_000_cont_0_storage.json --rpc https://granadanet.smartpy.io
```

## Entrypoints

```
getRandomBetweenCallback
  parameters:
    _from: TNat
    _to: TNat
    callback_address: TAddress

  Get a random number between _from and _to using storage entropy. 
  Does a callback with the result to `callback_address`.

getRandomBetweenCallbackEntropy
  parameters:
    _from: TNat
    _to: TNat
    entropy: TNat
    callback_address: TAddress

  Get a random number between _from and _to using passed entropy.
  Entropy is represented by a TNat number. 
  Does a callback with the result to `callback_address`.
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

  Get a random number between _from and _to using passed entropy. 
```


## TODO

* Look into rejection sampling
* Entrypoint to get multiple values (unique / non-unique optionally)

enjoy. 
