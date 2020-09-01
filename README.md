# Twitter Bot

This is a Twitter bot that is capable of retweeting non-retweets and non-replies from specific accounts.

## Requirements

To install the requirements from the project directory, run `pip install -r requirements.txt`.

## Required Files

In the `auth` directory, create a file called `credentials.json` based on the template provided and supply the required information.

In the `data` directory, create a file called `users.json` based on the template provided and supply the IDs of the users to retweet.

## Running

To run the program, use the command `python3 bot/bot.py` from the parent directory.

## Changes to Required Files

If your `credentials.json` or `filters.json` files have their contents changed, make sure you restart the application.