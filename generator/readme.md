- make a .env file with your `clashroyale_api_key=X`

Run ```download_swagger.py``` to  download the latest swagger.yaml file available.

As of 2025. A slight modification to the spec needs to be made to work with openAPI generator add the following before the paths: section around line 1317

```commandline
List:
  type: array
  items:
    type: object
```


Run the generator.py to generate new clash-royale clients