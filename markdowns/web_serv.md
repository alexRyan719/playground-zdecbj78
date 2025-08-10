# How do you display the results, in real time, so anyone at home can see the vote counts?

We would need a web server / website for every state, and maybe even every county for larger 
counties. This is relatively easy to do, as we're just working with linking databases to web 
servers as display only. The actual changes happen on the back end with emails in an email 
server (that has all the bells and whistles of cyber security Blue Teaming). Every vote is 
displayed as a line item that starts with the unique voter ID we create for every voter. 
By changing the hash every election and emailing a new one, it wouldn't matter if someone 
figured out who the person was behind the voter ID.

This would not only let them know it was counted, but counted accurately. If the vote isn't 
correct, the voter would send an email notifying the voter administrators. They would change 
the vote and log the change. There would be as many iterations of this as needed. Or, in 
other words, there would be a few "check again" corrections to the votes. This gives us 
traceable logs to investigate any fraud. Backup email addresses could be requested and those
emails used to confirm identity (other registered voter that will vouch, held accountable for
fraud). Or, any other combination of investigion tactics are possible with email logs and headers.

Test
