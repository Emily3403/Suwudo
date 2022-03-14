# girl-ify your sudo experience.

The default sudo insults assume the viewer is male. I've been increasingly offended by that and decided to change this
behaviour.

## How does it work?

For me recompiling sudo is a no-go. You open yourself up to all sorts of exploits, which I really don't want. So I have
created an in-place modificator that works with the current sudo installation.

This way we gain the benefit of not having to maintain an own sudo while still getting uwu output!

## Danger mitigation: root shell

First make sure to open a root-shell just to be sure. You're messing with `sudo` here and, if you shoot yourself in the
foot, you want to be able to recover. To do so type the following into your favorite shell

```shell
sudo su
```

Now just leave it open until the installation ends. If anything is fucked up, you can restore everything by typing the
following
*into the root shell*:

```shell
cp /usr/lib/sudo/sudoers.so.bak /usr/lib/sudo/sudoers.so
```

## Installation

Install with the following

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