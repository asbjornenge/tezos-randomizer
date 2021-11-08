import smartpy as sp
import json

Randomizer = sp.io.import_script_from_url("file:randomizer.py")
harbingerAddress = sp.address('KT1MwuujtBodVQFm1Jk1KTGNc49wygqoLvpe')

randomizerMetadata = {
  "name": "Randomizer",
  "description": "Tezos Oracle that can callback a random number between X and Y",
  "version": "1.0.0",
  "authors": ["asbjornenge <asbjorn@tezid.net>"]
}

sp.add_compilation_target("randomizer", Randomizer.Randomizer(
  harbingerAddress, 
  "XTZ-USD",
  metadata = sp.big_map(
    {
      "": sp.utils.bytes_of_string("tezos-storage:content"),
      "content": sp.utils.bytes_of_string(json.dumps(randomizerMetadata))
    }
  )
))