### Hexlet tests and linter status:
[![Actions Status](https://github.com/R3D3r3d3/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/R3D3r3d3/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/34a63e80f06af6bc440f/maintainability)](https://codeclimate.com/github/R3D3r3d3/gendiff-hexlet/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/34a63e80f06af6bc440f/test_coverage)](https://codeclimate.com/github/R3D3r3d3/gendiff-hexlet/test_coverage)

## USAGE

you have 2 JSON files 

file_1.json:
```{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
```

file_2.json:
```
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
```

and you can compare them in bash:
```
bash
>>> gendiff file_1.json file_2.json
{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}
 ```