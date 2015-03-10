queue = []
seen = {}
goal = 0

def getState () :
	global queue
        "return next state and pop it off the queue"
        
        if not queue : return None
        state = queue[0]
        queue = queue[1:]
        return state
def addState (parentState, newState) :
	global scene
        "add state if it's new. Remember its parent"
        if seen.has_key(str(newState)) : return
        seen[str(newState)] = str(parentState)
        queue.append (newState)
        #print '--- Adding ', newState
def getSolution () :
        "Return solution from latest state added"
        solution = []
        state = queue[-1]
        while state :
            solution.append (str(state))
            state = getParent(state)
        solution.reverse()
        return solution
def getParent (childState) :
        """return parent of state, if it exists"""
        try    : return seen[str(childState)]
        except : return None


def test (oldstate, newstate) :
    [newA, newB] = newstate
    won = (newA == goal or newB == goal)
    addState (oldstate, newstate)
    return won

def playGame (aMax, bMax, goal1) :
    	"grab a state and generate 8 more to submit to the manager"
    	global goal
	goal = goal1
    	addState("",[0,0])   # start with 2 empty buckets
        while 1 :
            oldstate = getState()
            [aHas,bHas] = oldstate
            if test (oldstate,[aMax,bHas]): break # fill A from well
            if test (oldstate,[0,bHas]): break # empty A to well
            if test (oldstate,[aHas,bMax]): break # fill B from well
            if test (oldstate,[aHas,0]): break # empty B to well
            howmuch = min(aHas,bMax-bHas)
            if test (oldstate,[aHas-howmuch,bHas+howmuch]): break # pour A to B
            howmuch = min(bHas, aMax-aHas)
            if test (oldstate,[aHas+howmuch,bHas-howmuch]): break # pour B to A
        print "Solution is "
        print "\n".join(getSolution())

playGame(7,11,6);
