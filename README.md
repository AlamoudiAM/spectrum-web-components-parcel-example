This code is playground for testing the integration of web components and Vue in raw HTML while still using modern web (npm, antd, parcel = babel + code splitting + caching). The goal is to use the result html in Django template while letting Django handle passing data, url routing, and authentication without the need of DRF.

```bash
yarn
python3 parcel-process.py
```

Final thought: It works except the bundle size build is large compare to Webpack and CRA (luckily should be fixed in Parcel v2).