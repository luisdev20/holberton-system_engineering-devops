## Shell permissions
In this section we are going to use the following *scripts*

0-iam_betty
su betty
Create a script that changes your user ID to betty.

1-who_am_i
id -un
Write a script that prints the effective userid of the current user.

2-groups
groups
Write a script that prints all the groups the current user is part of.

3-new_owner
sudo chown hello betty
Write a script that changes the owner of the file hello to the user betty.

4-empty
touch hello
Write a script that creates an empty file called hello.

5-execute
chmod 764 hello
Write a script that adds execute permission to the owner of the file hello.

6-multiple_permissions
chmod 554 hello
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody
chmod 711 hello
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello

8-James_Bond
chmod 007 hello
Write a script that sets the permission to the file hello

9-John_Doe
chmod 753 hello
Write a script that sets the mode of the file hello
