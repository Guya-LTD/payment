db.createUser(
    {
        user : "payment_user",
        pwd  : "payment_password",
        roles : [
            {
                role : "readWrite",
                db   : "payment_db"
            }
        ]
    }
)