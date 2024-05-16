### Hexlet tests and linter status:
[![Actions Status](https://github.com/R3D3r3d3/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/R3D3r3d3/python-project-50/actions)

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