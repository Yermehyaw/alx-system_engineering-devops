# Create a file in a server with puppet

file { '/tmp/school':
     ensure => file,
     owner => 'www-data',
     grpup => 'www-data',
     mode => '0744',
     content => ' I love Puppet'
}