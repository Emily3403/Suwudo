# UwU-ify your sudo experience.

Sudo answers are boring and assume the viewer is male. We can't have that.

## How does it work

For me recompiling sudo is a no-go. You open yourself up to all sorts of exploits, which I really don't want. So I have
created an in-place modificator that works with the current sudo installation.

This way we gain the benefit of not having to maintain an own sudo while still getting uwu output!

## Backup

Make sure to back up the original file first

```shell
sudo cp /usr/lib/sudo/sudoers.so ./sudoers.so.bak
```

If any problems arise you can simply log in as the root user and copy the files back.

## Install

First create your own patched library with

```shell
git clone --depth 1 https://github.com/Emily3403/Suwudo
cd Suwudo
```

Now you could make changes to the strings for example uwu-ify them even more ^-^

To create the library run

```
./suwudo.py
```

Finally, if everything exited successfully, you can now install the library

```
sudo cp sudoers.so /usr/lib/sudo/sudoers.so
```

Note: They may arise an error like

```
Job 1, 'sudo cp sudoers.so /usr/lib/sud…' terminated by signal SIGSEGV (Address boundary error)
```

when copying. This is kinda normal or doesn't influence the problem enough :D So just ignore it.

## Running sudo

You can try out the insults by opening a new terminal and executing

```shell
sudo su
```

Now fail a few times :D

## Future ideas

- sudo terminates after 3 wrong attemds
- Bring this to the arch user repository
- ansible config