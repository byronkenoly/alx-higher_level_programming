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
    query = session.query(State)

    """
    execute query
    """
    result = query.first()

    """
    print result
    """
    if result is None:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))

    """
    close session
    """
    session.close()
