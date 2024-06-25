# Repro for issue 7352

## Versions

platform: macOS Sonoma 14.5<br>
firebase-tools: v13.11.4<br>
gcloud: v476.0.0<br>
cloud-datastore-emulator: v2.3.1

## Steps to reproduce

1. Run `python3.11 -m venv venv`
   - Note: You might have a different version of python installed, try replacing `python3.11` with `python3.12`, or `python<VERSION>`
1. Run `. ./venv/bin/activate`
1. Run `pip install -r requirements.txt `
   - Installs the `requests` library
1. Open a separate terminal and run `gcloud emulators firestore start --host-port=127.0.0.1:50579 --database-mode=datastore-mode`
1. Run `python3 main.py`
   - Prints

```
{'batch': {'entityResultType': 'FULL', 'moreResults': 'MORE_RESULTS_AFTER_LIMIT', 'readTime': '2024-06-25T10:16:59.550825Z'}}
```

## Notes

1. When using `gcloud --project=test-app beta emulators datastore start --use-firestore-in-datastore-mode --host-port=127.0.0.1:50579`
1. Run `. ./venv/bin/activate`
   - You don't have to do this if you're already ran `. ./venv/bin/activate`
1. Running `python3 main.py`
   - Prints

```
{'batch': {'entityResultType': 'FULL', 'endCursor': 'CgA=', 'moreResults': 'MORE_RESULTS_AFTER_LIMIT'}}
```
