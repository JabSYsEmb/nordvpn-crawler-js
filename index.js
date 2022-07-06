#!/usr/bin/env node

const axios = require('axios');
const fs = require('fs');
const jsdom = require("jsdom");

const get_ovpn_urls = async function() {
	await axios.get('https://nordvpn.com/ovpn/').then(
	res => 
		{
		var doc = new jsdom.JSDOM(res.data, "text/xml");
			console.log(doc.window.document.querySelectorAll("body > div.Article > div > div > div > div > div > ul > li  > div > div > div > a").forEach(item => 
				{
					get_ovpn(item.href)
				}
			))
		}
	).catch(err => console.log(err))
}

// Start function
const get_ovpn = async function(url) {
	let date = new Date();
	console.log(url)
	const [month, day, year]       = [date.getMonth(), date.getDay(), date.getFullYear()];
	const [hour, minutes, seconds] = [date.getHours(), date.getMinutes(), date.getSeconds()];
	const ress = await axios.get(
				`${url}`,
				{
					headers: 
					{
						"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
						"accept-language": "en-US,en;q=0.9,ar;q=0.8",
						"sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
						"sec-ch-ua-mobile": "?0",
						"sec-ch-ua-platform": "\"macOS\"",
						"sec-fetch-dest": "document",
						"sec-fetch-mode": "navigate",
						"sec-fetch-site": "cross-site",
						"sec-fetch-user": "?1",
						"upgrade-insecure-requests": "1",
						"Referer": "https://nordvpn.com/",
						"Referrer-Policy": "strict-origin-when-cross-origin"
					},
					"body": null,
					"method": "GET"
				}
			)
			.then(res => {
				const file_name = res.request.path.split('/').pop()
				fs.writeFileSync(`data/${file_name}`,res.data)
				 console.log(`${file_name} downloaded succesfully.`)
			})
			.catch(_ => {
				console.log(`${url} isn't working`)
			})
}

get_ovpn_urls()
