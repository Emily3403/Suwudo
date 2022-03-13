# UwU-ify your sudo experience.

Sudo answers are boring and assume the viewer is male. We can't have that.

## How does it work

For me recompiling sudo is a no-go. You open yourself up to all sorts of exploits, which I really don't want.
So I have created an in-place modificator that works with the current sudo installation.

This way we gain the benefit of not having to maintain an own sudo while still getting uwu output!

## Installation

Create your own `sudoers.so` library with 
```shell
./suwudo.py
```

Now a file `sudoers.so` will appear in your cwd.

Copy it to the destination with
```shell
cp sudoers.so /usr/lib/sudo/sudoers.so
```
