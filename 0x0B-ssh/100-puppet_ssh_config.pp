# Puppet file to configure client ssh_config file

class ssh_config {
      $config_content = @(EOT)
      		      Host *
      		      	   HostName 35.153.52.184
		      	   Port 22
		      	   User ubuntu
		      	   PasswordAuthentication no
		      	   IdentityFile ~/.ssh/school
	EOT

	file { '/etc/ssh/ssh_config':
            ensure => file,
      	    owner => 'root',
      	    group => 'root',
      	    mode => '755',
      	    content => $config_content
      }
}

include ssh_config