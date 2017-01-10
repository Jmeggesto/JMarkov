#JMarkov

A Markov chain generator that shitposts the things I've said on
IRC in the past 6 months to Twitter.

##Why Did You Write This?

Because I could. Because I was bored. 

##What Did You Use?

I used [Markovify](https://github.com/jsvine/markovify) for the Markov parts and
[Twython](https://github.com/ryanmcgrath/twython) for posting to Twitter. I have a crontab running
on a DigitalOcean droplet to take care of periodically posting tweets.

##Where Did The Corpus Come From?

My IRC client logs to my computer by default, so I just parsed the logs into a nice,
neat format and put the text file on the VPS, which is where mgenerate.py reads from.

##Are You Crazy? 

Yeah.
