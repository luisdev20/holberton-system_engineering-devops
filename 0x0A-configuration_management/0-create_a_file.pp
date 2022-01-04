# Using puppet to create a file in /temp

file { 'holberton':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}