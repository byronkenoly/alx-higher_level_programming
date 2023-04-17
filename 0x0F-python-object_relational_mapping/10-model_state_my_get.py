#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    create engine and session
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    create query
    """
    name = sys.argv[4]
    query = session.query(State).filter(State.name.like(name)).order_by(State.id)

    """
    execute query
    """
    result = query.all()

    """
    print result
    """
    if len(result) == 0:
        print("Not found")
    else:
        print("{}".format(result[0].id))

    """
    close session
    """
    session.close()
