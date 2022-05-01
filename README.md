
# Kwiss

A Project for learning kivy. 
It's a basic Quiz app: Just define question and answer and start to learn (see *[Build](#Build "Goto section 'Build'")*)



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

By the time I wrote this, there's no way of defining vocabulary sets (or any 'question-answer pairs') from within the running application.
One'd have to add them to '[src/resource/lat.py](https://github.com/lrshsl/kwiss/blob/android/src/resource/lat.py "Open File")', before compiling.
In parser_mod though, there's a parser which is capable of translating some formats to the needed format.



## Progress

- [X] Basic functionality
  - [X] Show question
  - [X] Get input
  - [X] Process input
  - [X] React(false: again, true: next)

- [ ] Asthetics
  - [ ] Loading screen
  - [ ] Start screen
  - [ ] Transitions?

- [ ] Additional functionality
  - [ ] Tolerance (What answers to accept)
  - [ ] Add questions from within the app

- [ ] Settings
  - [ ] Tolerance (What answers to accept)
  - [ ] Look & Feel?
