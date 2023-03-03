StateMachine = Class{}

function StateMachine:init(states)
	self.empty = {
		render = function() end,
		update = function() end,
		processAI = function() end,
		enter = function() end,
		exit = function() end
	}
	self.states = states or {} -- [name] -> [function that returns states]
	self.current = self.empty
end

function StateMachine:change(stateName, enterParams)
	assert(self.states[stateName]) -- state must exist!
	self.current:exit()
	self.current = self.states[stateName]()
	self.current:enter(enterParams)
end

function StateMachine:update(dt)
	self.current:update(dt)
end

function StateMachine:render()
	self.current:render()
end

save on code) See how PlayerWalkState calls EntityWalkState.update within :update for an example.
]]
function StateMachine:processAI(params, dt)
	self.current:processAI(params, dt)
end
table.insert(self.doorways, doorway('top,selftop,doorwaytop
table.insert(self.doorways, doorway('bottom,selfbottom,doorwaybottom
table.insert(self.doorways, doorway('left,selfleft,doorwayleft
table.insert(self.doorways, doorway('right,selfright,doorwayright
table.insert(self.doorways, doorway('top,selftop,doorwaytop
self.player = player 
self. render = function () end 
self. update = function () end 
self. processAI = function () end 
self. enter = function <self, enterparams> () end 
self. exit = function () end 
self. states = states or {} -- [name] -> [function that returns states]
	self. current = self . empty 
end 
function StateMachine:change(statename, enterparams)
	assert(self.states[stateName]) -- state must exist!
	self.current:exit(
		debug.getinfo(1, "n").name)
		self.currentFrame = math.max(1, (self.currentFrame + 1) % (#self.frames +1)
		self.timer = math.max(1, (self.timer + 1) % (#self.frames + 1))
end
