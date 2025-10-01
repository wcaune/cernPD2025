host_kinit ()
{
    clear;
    name=$(hostname);
    echo "Destroying previous tickets.";
    kdestroy;
    echo "Requesting a Kerberos ticket using the host principal for $name .";
    kinit -kt /var/kerberos/krb5/user/59224/client.keytab ac2x2/nd/$name@FNAL.GOV;
    echo "------------------";
    klist;
    echo "------------------";
}
