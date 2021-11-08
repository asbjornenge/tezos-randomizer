# Tezos Randomizer

Tezod Randomizer "Oracle".  

It's a smart contract that you can call to get a random number between X and Y (for now).

It uses entropy from `timestamp` at calltime AND the [Harbinger Oracle](https://github.com/tacoinfra/harbinger).

## Contracts

* Granadanet
  * [KT18nMUHUjAHmJBYR2kSFASCCp9e4xzCNKzk](https://better-call.dev/granadanet/KT18nMUHUjAHmJBYR2kSFASCCp9e4xzCNKzk/)

## Import

```
Randomizer = sp.io.import_script_from_url("https://ipfs.infura.io/ipfs/QmeQ8QUmbQ1oV9FQb65UxgbM5323yuKNFgk3WgTzgzeY3E")
```

## Setup environment

```
./scipts/init-env.sh
source bin/activate
spy test tests.py output --html
```

## Compile & Deploy

```
spy compile compile.py compiled
spy originate-contract --code compiled/randomizer/step_000_cont_0_contract.tz --storage compiled/randomizer/step_000_cont_0_storage.json --rpc https://granadanet.smartpy.io
```

## TODO

* Get fresh entropy on Request
* Hangzhou views :tada:
* Add more entropy (other sources too)
* Look into rejection sampling
* Expose more entrypoints

enjoy. 
