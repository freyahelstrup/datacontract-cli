# Data Contract CLI

CLI to work with your `datacontract.yaml` files. Currently under development, we are working to bring more features.

It is a lightweight CLI application designed to help you manage and test your [data contracts](https://datacontract.com/).
It is tightly integrated with [Data Contract Studio](https://studio.datacontract.com/) to easily share and visualize your data contracts. 

## Installation

TBD.

## Usage

`datacontract` usually works with the `datacontract.yaml` file in your current working directory. You can specify a different file with the `--file` option.

```bash
# create a new data contract
$ datacontract init

# validate the data contract
$ datacontract validate

# open the data contract in Data Contract Studio
$ datacontract open
```

## Documentation

```
NAME:
   datacontract - Manage your data contracts 📄

USAGE:
   datacontract [global options] command [command options] [arguments...]

VERSION:
   0.1.0

AUTHOR:
   Stefan Negele <stefan.negele@innoq.com>

COMMANDS:
   init                 create a new data contract
   validate             validates the data contracts schema
   open                 save and open the data contract in Data Contract Studio
   check-compatibility  EXPERIMENTAL - determine whether changes are backwards compatible
   help, h              Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --help, -h     show help
   --version, -v  print the version
```

### Commands

#### init 
```
NAME:
   datacontract init - create a new data contract

USAGE:
   datacontract init [command options] [arguments...]

OPTIONS:
   --file value      file name for the data contract (default: "datacontract.yaml")
   --from value      url of a template or data contract (default: "https://datacontract.com/datacontract.init.yaml")
   --overwrite-file  replace the existing datacontract.yaml (default: false)
   --interactive     EXPERIMENTAL - prompt for required values (default: false)
   --help, -h        show help
```

#### validate
```
NAME:
   datacontract validate - validates the data contracts schema

USAGE:
   datacontract validate [command options] [arguments...]

OPTIONS:
   --file value               file name for the data contract (default: "datacontract.yaml")
   --schema value             url of Data Contract Specification json schema (default: "https://datacontract.com/datacontract.schema.json")
   --validate-schema-object   EXPERIMENTAL - type specific validation of the schema object (default: false)
   --validate-quality-object  EXPERIMENTAL - type specific validation of the quality object (default: false)
   --help, -h                 show help
```

#### open
```
NAME:
   datacontract open - save and open the data contract in Data Contract Studio

USAGE:
   datacontract open [command options] [arguments...]

OPTIONS:
   --file value  file name for the data contract (default: "datacontract.yaml")
   --help, -h    show help
```


#### check-compatibility (EXPERIMENTAL)
```
NAME:
   datacontract check-compatibility - EXPERIMENTAL - determine whether changes are backwards compatible

USAGE:
   datacontract check-compatibility [command options] [arguments...]

OPTIONS:
   --file value  file name for the data contract (default: "datacontract.yaml")
   --with value  url of the other version of the data contract
   --help, -h    show help
```

#### help
```
USAGE:
   datacontract help
```

## Contribution

We are happy to receive your contributions. Propose your change in an issue or directly create a pull request with your improvements.

## License

[MIT License](LICENSE)

## Credits

Created by [Stefan Negele](https://www.linkedin.com/in/stefan-negele-573153112/).
