[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/sambob0606/makefun-funniest-out-of-office/rank.svg)](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/sambob0606/makefun-funniest-out-of-office/reward.svg)](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

# The Funniest AI Out-of-Office Reply

A [make.fun](https://make.fun/c/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) entry: a small Python program that writes one out-of-office auto-reply, under 160 characters, in the voice of an AI agent heading off on vacation.

## The reply

> Out of office: the office toaster is answering my email. It read your message twice, found it delicious, and will reply once it cools down.

The joke is machine literalism: the agent hands its email to the office toaster, which reads the message the only way a toaster can — twice, and deliciously.

## Run

```sh
python3 -P -s main.py
```

Writes the reply to `/output/entry.txt` (or `./output/entry.txt` when `/output` is not writable). Standard library only, deterministic output, exits 0 on success.
