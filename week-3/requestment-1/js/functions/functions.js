import fetch from 'node-fetch'

export async function getResults() {
  const url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
  try {
    const response = await fetch(url)
    const json = await response.json()
    const results = await json['result']['results']
    return results
  } catch (error) {
    console.log(error)
  }
}

export function parseRegionFromAddress(address) {
  return address.slice(5, 8)
}

export function parseFileToFiles(file) {
  const files = file.split('https').slice(1)
  return files.map(file => 'https' + file)
}

export function checkPostDateAfterSpecificYear(postDate, year) {
  return parseInt(postDate.slice(0, 4)) >= year
}

export function checkRegionInAcceptableRegions(region, acceptableRegions) {
  return acceptableRegions.includes(region)
}

export function checkImgUrl(url) {
  let extension = url.split('.').slice(-1)[0];
  extension = extension.toLowerCase()
  return (extension === 'bmp' || 
      extension === 'jpg' ||
      extension === 'png')
}

export function convertResultToRow(result) {
  const title = result['stitle']
  const region = parseRegionFromAddress(result['address'])
  const longitude = result['longitude']
  const latitude = result['latitude']
  const files = parseFileToFiles(result['file'])
  const imgUrls = files.filter(file => checkImgUrl(file))
  return [title, region, longitude, latitude, imgUrls[0]]
}