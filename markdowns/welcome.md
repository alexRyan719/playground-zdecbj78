# Welcome!

First off, this is not meant to be political in any way. Rather, this is a potential solution to the ugliness politics has often become. 
If this is done correctly, it should be able to be used in any country, state, province, territory, county, city, region. 

How does it work?

The idea is to allow registered voters to use their email account to cast their vote. First, every registered voter would need to link an email address 
to their government ID. This should be done in person, but can be updated with a video call (Google Meets, Zoom, etc). A hash can be generated for every 
election or however frequently is needed. The government ID numbers should still stay hidden, but the email and the name can be less protected.

Why Email?

Most email servers allow Multi Factor Authentication. As long as the email account is protected with strong MFA (authenticator apps are preferred, passkeys should be available / robust soon).
Once you have a trusted accounting of only one valid email address per registered voter, you can prove that only currently registered voters are able to vote. 

Below is an example of how to generate a simple hash for a unique voter ID. This would be sent to each registered voter. The voter would respond to that email with their
vote. By using a newly generated hash every election (date or election id can be added to the hash input), you can post a list of all those IDs and the corresponding
vote on websites. After the polls close, every voter would be asked to check that their vote is accurate. They would copy the hash ID from their email, do a find
on the website for it, and verify their vote is accurate. This would not only let them know it was counted, but counted accurately. If the vote isn't correct, the
voter would send an email notifying the voter administrators. They would change the vote and log the change. There would be as many iterations of this as needed.
Or, in other words, there would be a few "check again" corrections to the votes. This gives us traceable logs to investigate any fraud. Backup email addresses could 
be requested and those emails used to confirm identity (other registered voter that will vouch, held accountable for fraud). Or, any other combination of investigion
tactics are possible with email logs and headers.

Generate a Unique User ID

@[This makes a unique hash out of pieces of information, like first name, last name, state, etc]({"stubs": ["test.py"], "command": "python3 test.py"})

