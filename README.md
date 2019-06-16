> Tested on Ubuntu 18.04 

### How to install docker 
* [Install on Mac](https://docs.docker.com/docker-for-mac/install/)
* [Install on Windows](https://docs.docker.com/docker-for-windows/install/)
* [Install on Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

**NOTE** For Ubuntu or any Linux installation for that matter, notice the [Post-Installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/)

### Run on Host machine
0. Install [Anaconda](https://www.anaconda.com/distribution/) depending on your OS.
1. `cd src`
2. `conda env create -f envionment.yml`
3. `conda activate infinite-scroll`
4. `python infinite-scroll.py`


##TODOs: 
- not as straightforward as one thought, needs to map some stuff to the container. 
- or an alternative would be start `FROM` a selenium base image and add my stuff there. 

### Run in a Docker container
0. Install docker (see links at the top)
1. `docker build -t infinite-scroll .`
2. `docker run -it -v output:/output infinite-scroll`
3. `conda activate infinite-scroll`
4. `python infinite-scroll.py`

After a longtime or short time depending on how infinite it is.... Your output should be in /output if you are inside the container, or ./output once you exit the container and on your host machine.



<details><summary>Helpful links</summary>

- [ ] https://github.com/SeleniumHQ/docker-selenium
- [ ] https://www.qatouch.com/blog/how-to-run-selenium-webdriver-with-docker/
- [ ] https://github.com/mozilla/geckodriver/releases/tag/v0.24.0

> How to create an infinite scroll site, (please don't...) unless you are building a social media site or some kinda story telling site. 
- [ ] https://el-tramo.be/blog/infinite-scroll/
- [ ] https://code.tutsplus.com/tutorials/how-to-create-infinite-scroll-pagination--wp-24873

> Web Scrapping with Selenium + Python
- [ ] https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72
- [ ] https://www.agenty.com/blog/how-to-crawl-an-infinite-scrolling-ajax-website
- [ ] https://www.accordbox.com/blog/how-crawl-infinite-scrolling-pages-using-python/

> Other tools
- [ ] https://intoli.com/blog/scrape-infinite-scroll/


</details>
