# Twitter Bot

This is a Twitter bot that is capable of retweeting non-retweets and non-replies from specific accounts.

## Requirements

To install the requirements from the project directory, run `pip install -r requirements.txt`.

## Required Files

In the `auth` directory, create a file called `credentials.json` based on the template provided and supply the required information.

In the `data` directory, create a file called `users.json` based on the template provided and supply the IDs of the users to retweet.

In the `data` directory, create a file called `settings.json` based on the template provided and supply the settings desired.

## Supported Settings

These are the currently supported settings (in `settings.json`) and the values they can take.
- log_level: Specifies the level of logging to display in the log file. Supported values are `warning`, `info`, and `error`. Invalid values will default to `error`.

## Running

To run the program, use the command `python3 bot/bot.py` from the parent directory.

## Logging

Log contents will be output to `log.txt` in the top-level directory of the repository.

## Changes to Required Files

If your `credentials.json`, `filters.json`, or `settings.json` files have their contents changed, make sure you restart the application.