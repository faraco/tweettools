# tweettool

A command line program to automate Twitter common usage.

## Getting Started

### Prerequisites
* python3
* twitter

> You can install the dependencies via pip using `pip install -r requirements.txt`

### Running the program

Run `python3 tweettool.py -h` to see the available options.

## Running the tests

> You *must* assign `T_CONSUMER_KEY`, `T_CONSUMER_SECRET`, `T_ACCESS_TOKEN`, `T_ACCESS_TOKEN_SECRET`, `T_HANDLE` environment variables with your Twitter's consumer key, consumer secret, access_token, access_token_secret, and twitter handle.

To run the tests, you can run `python -m unittest discover tests`

or with nose: `nosetests`

## Authors

* [faraco](https://github.com/faraco) <skelic3@gmail.com>
        
## License

This project is licensed under the GPL3 License - see the LICENSE file for details.
