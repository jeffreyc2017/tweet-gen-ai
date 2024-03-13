# TweetGenAI

TweetGenAI is a Python-based bot designed to generate and post content automatically to X (formerly Twitter) using OpenAI's GPT models. It leverages the Twitter API for posting and is configurable to post at predefined intervals.

## Features

- Automated tweet generation using AI.
- Customizable posting intervals.
- Easy configuration through environment variables.
- Supports both text-based content generation and potential integration with other APIs for enriched content.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Tweepy
- python-dotenv

### Installation

1. Clone the repository:

```bash
git clone https://github.com/jeffreyc2017/tweet-gen-ai.git
```

2. Navigate to the project directory:

```bash
cd tweet-gen-ai
```

3. Install the required packages:

```bash
pip install tweepy python-dotenv openai
```

4. Create a `.env` file in the root directory with your Twitter API credentials and other configuration settings:

```
API_KEY=your_api_key_here
API_SECRET_KEY=your_api_secret_key_here
ACCESS_TOKEN=your_access_token_here
ACCESS_TOKEN_SECRET=your_access_token_secret_here
```

### Usage

1. Modify `main.py` as needed to customize the tweet generation logic.

2. Run the bot:

```bash
python main.py
```

## Running the tests

To run the tests, execute the following command in the project directory:

```bash
python unit_test.py
```

## Deployment

[Deployment](deployment.md)

## Built With

- [Python](https://www.python.org/) - The programming language used.
- [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.
- [python-dotenv](https://github.com/theskumar/python-dotenv) - A Python library for managing environment variables.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jeffreyc2017/tweet-gen-ai/tags).

## Authors

- **Jeffrey Cai** - *Initial work* - [jeffreyc2017](https://github.com/jeffreyc2017)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgments
