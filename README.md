NextEx is a simple dating app that matches users based on the compatibility of their astrological sign. 

Users will be able to: 
- Create a user profile
- Retrieve matches based on astrological sign
- Update account (description, photos, drop down choices)
- View matches in a match bar
- Delete your account when you’ve found your next ex!


Domain Model: <br></br>
![Screenshot 2023-10-26 at 10 39 09 AM](https://github.com/kristi-panko-flatiron/NextEx/assets/136921157/f8b30ab4-0297-4ebb-bee9-fabb41e3d666)
<br></br>

Wireframe:<br></br>
![Screenshot 2023-10-26 at 10 42 28 AM](https://github.com/kristi-panko-flatiron/NextEx/assets/136921157/54c57dfe-01ad-4a46-8cd3-7373eddf0687)

Relationships:
A user can have one astrological sign (one-to-one relationship).<br></br>
A user can have UserMatch (one-to-many relationship).<br></br>
AstrologicalSign Table:<br></br>
An astrological sign can be associated with multiple users (one-to-many relationship).<br></br>
Each astrological sign has a set of best matches associated with it (one-to-one relationship with AstrologicalCompatibility).<br></br>
UserMatch Table (Intermediary Table):<br></br>
Records the matches between users. It establishes a many-to-many relationship between users.<br></br>
Match Table:<br></br>
Represents the matches between users. Records the date of the match.<br></br>
Maintains a record of user matches through the UserMatch table.<br></br>
BestMatch Table:<br></br>
Stores information about the best matches for each astrological sign.<br></br>
Each astrological sign can be associated with multiple best matches, forming a one-to-many relationship.


Routing:<br></br>
GET /users/:id<br></br>
POST /users/<br></br>
PUT /users/:id<br></br>
DELETE /users/:id<br></br>
GET /astrological_signs/:id<br></br>
POST /astrological_signs/<br></br>
PUT /astrological_signs/:id<br></br>
DELETE /astrological_signs/:id<br></br>
GET /matches/:id<br></br>
POST /matches/<br></br>
PUT /matches/:id<br></br>
DELETE /matches/:id<br></br>
GET /astrological_compatibility/:id<br></br>
POST /astrological_compatibility/<br></br>
PUT /astrological_compatibility/:id<br></br>
DELETE /astrological_compatibility/:id<br></br>

Validations: 
Must have a name<br></br>
Must have username<br></br>
Must have valid password<br></br>
Must have valid astrological sign<br></br>
Must have an age between 18-99<br></br>


USER: (‘-user_match.user’,)<br></br>
AstroSign (-user.astrological_sign’,)<br></br>
Match (‘-user.user_matches’,)<br></br>
UserMatch (‘-user.user_matches’, ‘-match.user_matches’,)<br></br>



Stretch goals:<br></br>
Match users also based on location<br></br>
Allow users to link their social media profiles<br></br>
Integrate a feature that suggests dates based on location<br></br>
