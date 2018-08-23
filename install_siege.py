def func(self):
    """
    # wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    # rpm -Uvh ./epel-release-6-8.noarch.rpm
    Preparing...                ########################################### [100%]
    package epel-release-6-8.noarch is already installed
    """
    import sh
    sh.sudo.yum("install", "-y", "wget")
    sh.wget("http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
    try:
        sh.sudo.rpm("-Uvh", "./epel-release-6-8.noarch.rpm")
    except sh. ErrorReturnCode_1, e:
        self.warn(self.rid, str(e))
    finally:
        r=sh.sudo.yum("install", "-y", "siege")
    return r
