## Install

* Install `ruby` and `bundler`

```bash
bundle install --path vendor/bundle
```
(You need to have ruby and bundler installed on your system)

## Build the document
```bash
./generate.sh main.adoc
```

## Source structure

* `main.adoc`: Main document
* `/dist`: Output document (both HTML and PDF) will be generated here
* `/imgs`: Put image files here
