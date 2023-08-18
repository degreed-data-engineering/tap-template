# `tap-xtm`
This tap xtm was created by Degreed to be used for extracting data via Meltano into defined targets.

## Testing locally

To test locally, pipx poetry
```bash
pipx install poetry
```

Install poetry for the package
```bash
poetry install
```

To confirm everything is setup properly, run the following: 
```bash
poetry run tap-xtm --help
```

To run the tap locally outside of Meltano and view the response in a text file, run the following: 
```bash
poetry run tap-xtm > output.txt 
```

A full list of supported settings and capabilities is available by running: `tap-xtm --about`

## Config Guide

To test locally, create a `config.json` with required config values in your tap_xtm folder (i.e. `tap_xtm/config.json`)

```json
{
  "api_key": "$DD_API_KEY",
  "app_key": "$DD_APP_KEY",
  "start_date": "2022-10-05T00:00:00Z"
}
```

**note**: It is critical that you delete the config.json before pushing to github.  You do not want to expose an api key or token 

### Add to Meltano 

The provided `meltano.yml` provides the correct setup for the tap to be installed in the data-houston repo.  

At this point you should move all your updated tap files into its own tap-xtm github repo. You also want to make sure you update in the `setup.py` the `url` of the repo for you tap.

Update the following in meltano within the data-houston repo with the new tap-xtm credentials/configuration.

```yml
plugins:
  extractors:
  - name: tap-xtm
    namespace: tap_xtm
    pip_url: git+https://github.com/degreed-data-engineering/tap-xtm
    capabilities:
    - state
    - catalog
    - discover
    config:
      api_key: $DD_API_KEY
      app_key: $DD_APP_KEY
      start_date: '2022-10-05T00:00:00Z'
 ```

To test in data-houston, run the following:
1. `make meltano` - spins up meltano
2. `meltano install extractor tap-xtm` - installs the tap
3. `meltano invoke tap-xtm --discover > catalog.json` - tests the catalog/discovery
3. `meltano invoke tap-xtm > output.txt` - runs tap with .txt output in `meltano/degreed/`

That should be it! Feel free to contribute to the tap to help add functionality for any future sources
## Singer SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/index.html) for more instructions on how to use the Singer SDK to develop your own taps and targets.