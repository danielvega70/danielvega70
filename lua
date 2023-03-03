push = require 'push'

VIRTUAL_WIDTH = 384
VIRTUAL_HEIGHT = 216

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

function love.load()
    currentSecond = 0
    secondTimer = 0

    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = true
    })
end

function love.resize(w, h)
    push:resize(w, h)
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end
end

function love.update(dt)
    secondTimer = secondTimer + dt

    if secondTimer > 1 then
        currentSecond = currentSecond + 1
        secondTimer = secondTimer % 1
    end
end

function love.draw()
    push:start()
    love.graphics.printf('Timer: ' .. tostring(currentSecond) .. ' seconds',
        0, VIRTUAL_HEIGHT / 2 - 6, VIRTUAL_WIDTH, 'center')
    push:finish()
end
function love.load()
    currentsecond = 0
    secondtimer = 0

    love.graphics.setDefaultFilter('nearest', `nearest`)
    push:setupscreen(virtual_width, VIRTUAL_HEIGHT, window_width, WINDOW_HEIGHT)
end
timer.tween(0.2, self, (x= 0, y= 0, w= virtual_width, h=virtual_height), 'out-quad', function()
    gstate.switch(game)
end)
pull:setupscreen(virtual_width,virtual_height,window_width,window_height,
full screen = false, vsync= true, resizable = true)
if key == 'escape' then
    love.event.quit()
    push :finish()
end 
