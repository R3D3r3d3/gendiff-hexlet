### Hexlet tests and linter status:
[![Actions Status](https://github.com/R3D3r3d3/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/R3D3r3d3/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/34a63e80f06af6bc440f/maintainability)](https://codeclimate.com/github/R3D3r3d3/gendiff-hexlet/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/34a63e80f06af6bc440f/test_coverage)](https://codeclimate.com/github/R3D3r3d3/gendiff-hexlet/test_coverage)

## USAGE

if you want to compare 2 JSON files 

1. For example 2 flat JSON:

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

2. Also you can compare flat YML, nested JSON, nested YML files and receive results
in stylish, plain text or in json:
```
>>>gendiff file1.yml file2.yml -f plain
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```
