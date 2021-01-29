## Shell permissions
In this section we are going to use the following *scripts*

0-iam_betty\n
su betty\n
Create a script that changes your user ID to betty.

1-who_am_i\n
id -un\n
Write a script that prints the effective userid of the current user.

2-groups\n
groups\n
Write a script that prints all the groups the current user is part of.

3-new_owner\n
sudo chown hello betty\n
Write a script that changes the owner of the file hello to the user betty.

4-empty\n
touch hello\n
Write a script that creates an empty file called hello.

5-execute\n
chmod 764 hello\n
Write a script that adds execute permission to the owner of the file hello.

6-multiple_permissions\n
chmod 554 hello\n
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody\n
chmod 711 hello\n
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello

8-James_Bond\n
chmod 007 hello\n
Write a script that sets the permission to the file hello

9-John_Doe\n
chmod 753 hello\n
Write a script that sets the mode of the file hello

10-mirror_permissions\n
chmod --reference=olleh hello\n
Write a script that sets the mode of the file hello the same as ollehs mode.

11-directories_permissions\n
chmod a+X *\n
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

12-directory_permissions\n
mkdir --mode=751 dir_holberton\n
Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.

13-change_group\n
chgrp holberton hello\n
Write a script that changes the group owner to holberton for the file hello

14-change_owner_and_group\n
sudo chown betty:holberton *\n
A script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

15-symbolic_link_permissions\n
sudo chown -h betty:holberton _hello\n
A script that changes the owner and the group owner of the file _hello to betty and holberton respectively.

16-if_only\n
sudo chown --from=guillaume betty hello\n
A script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
