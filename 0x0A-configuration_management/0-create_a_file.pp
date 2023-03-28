# Create a file in /tmp

file { 'SCHOOL':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
  path    => '/tmp/school',
}
