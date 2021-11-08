# Tezos Randomizer

Tezod Randomizer "Oracle".  

It's a smart contract that you can call to get a random number between X and Y (for now).

It uses entropy from `timestamp` at calltime AND the [Harbinger Oracle](https://github.com/tacoinfra/harbinger).

## Contracts

* Granadanet
  * [KT1NAn3Le3o3eJKdf6G49PjQ2cNVMeUW871R](https://better-call.dev/granadanet/KT1NAn3Le3o3eJKdf6G49PjQ2cNVMeUW871R/)

## Setup environment

```
./scipts/init-env.sh
source bin/activate
spy test tests.py output --html
```

## TODO

* Add more entropy (other sources too)
* Expose more entrypoints

enjoy. 
