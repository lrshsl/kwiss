
# Kwiss

A Project for learning kivy. 
It's a basic Quiz app: You can define question and answer and start to learn (see *[Build](#Build)*)



## Incentive

I started this project to learn the basics of both the python module [Kivy](https://kivy.org/#home "Kivy Homepage") and git/github.
I created it on Linux, and mainly for android, but since kivy is cross-platform, it shouldn't be a hassle to get it 
running on any of the supported platforms.

I'd welcome any kind of suggestions (e. g. codestyle, application design, ..), improvements (my english.. :\ ) or questions (I saw quite a few missleading error messages).



## Build

> Note: It's not recommended to try it yourself.
> I made this application for personal use only and I can't claim that I understand what I'm doing.
> The following instructions are primarily for me - so I don't forget which commands to run.

```fish
git clone (this url)
cd kwiss-android

vim ./release/buildozer.spec

buildozer -v android debug
buildozer android deploy run
```
