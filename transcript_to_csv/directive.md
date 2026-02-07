Your job is to read each txt file in this folder, then write each csv file in the following format:
```
from;to;speaker;content
```

Example:
```
00:00:54,160 --> 00:01:07,600 [speaker_1]
Uh, okay. Hi, everyone. I'm Donna, and, uh, I'm, uh, in animation major. Uh, I'm a freshman, uh, in my first year. Nice to meet everyone.

00:01:09,220 --> 00:01:11,520 [speaker_0]
Okay. How long have you been here?
```
translate into
```
from;to;speaker;content
00:00:54,160;00:01:07,600;1;Uh, okay. Hi, everyone. I'm Donna, and, uh, I'm, uh, in animation major. Uh, I'm a freshman, uh, in my first year. Nice to meet everyone.
00:01:09,220;00:01:11,520;0;Okay. How long have you been here?
```
