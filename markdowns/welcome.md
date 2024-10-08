# Welcome!

First off, this is not meant to be political in any way. Rather, this is a potential solution to the ugliness politics has often become. 
If this is done correctly, it should be able to be used in any country, state, province, territory, county, city, region. 

How does it work?

The idea is to allow registered voters to use their email account to cast their vote. First, every registered voter would need to link an email address 
to their government ID. This should be done in person, but can be updated with a video call (Google Meets, Zoom, etc). A hash can be generated for every 
election or however frequently is needed. The government ID numbers should still stay hidden, but the email and the name can be less protected. The votes 
would be mostly seen by computer / robot eyes only. The only times any humans would look at votes is if the voter claimed their vote was changed or inaccurate.

Why Email?

Most email servers allow Multi Factor Authentication. As long as the email account is protected with strong MFA (authenticator apps are preferred, passkeys 
should be available / robust soon), then we can guarantee only the actual registered voter has access. There are still ways to break MFA, but there are ways to
detect those ways. It's all traceable. Once you have a trusted accounting of only one valid email address per registered voter, you can prove that only currently 
registered voters are able to vote. 

Below is an example of how to generate a simple hash for a unique voter ID. This would be sent to each registered voter. The voter would respond to that email with their
vote. By using a newly generated hash every election (date or election id can be added to the hash input), you can post a list of all those IDs and the corresponding
vote on websites. After the polls close, every voter would be asked to check that their vote is accurate. They would copy the hash ID from their email, do a find
on the website for it, and verify their vote is accurate. 

How do you vote?

An email would be sent to every registered email address with an underscore next to each candidate's first name, last name, and party. The voter would copy the 
text and replace the underscore with an X (or literally anything else, even just erase the underscore). As long as it's not an underscore, it's marked as the 
selection. That reply is sent with the choices indicated. A machine would read incoming emails, check against a list of all emails, and then log the vote for 
the email address.That database entry would then be used to update the vote database. 

How do you display the results, in real time, so anyone at home can see the vote counts?

We would need a web server / website for every state, and maybe even every county for larger counties. This is relatively easy to do, as we're just working with
linking databases to web servers as display only. The actual changes happen on the back end with emails in an email server (that has all the bells and whistles
of cyber security Blue Teaming). Every vote is displayed as a line item that starts with the unique voter ID we create for every voter. By changing the hash 
every election and emailing a new one, it wouldn't matter if someone figured out who the person was behind the voter ID. 

This would not only let them know it was counted, but counted accurately. If the vote isn't correct, the
voter would send an email notifying the voter administrators. They would change the vote and log the change. There would be as many iterations of this as needed.
Or, in other words, there would be a few "check again" corrections to the votes. This gives us traceable logs to investigate any fraud. Backup email addresses could 
be requested and those emails used to confirm identity (other registered voter that will vouch, held accountable for fraud). Or, any other combination of investigion
tactics are possible with email logs and headers.

Generate a Unique User ID

@[This makes a unique hash out of pieces of information, like first name, last name, state, etc]({"stubs": ["test.py"], "command": "python3 test.py"})

