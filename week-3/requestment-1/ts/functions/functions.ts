import fetch from 'node-fetch'
import { Result } from './types'

export function getResults(): Promise<Result[]> {
  const url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
  return fetch(url)
    .then(response => response.json())
    .then(json => json['result']['results'] as Result[])
}

export function parseRegionFromAddress(address: string): string {
  return address.slice(5, 8)
}

export function parseFileToFiles(file: string): string[] {
  const files = file.split('https').slice(1)
  return files.map(file => 'https' + file)
}

export function checkPostDateAfterSpecificYear(postDate: string, year: number): boolean {
  return parseInt(postDate.slice(0, 4)) >= year
}

export function checkRegionInAcceptableRegions(region: string, acceptableRegions: string[]): boolean {
  return acceptableRegions.includes(region)
}

export function checkImgUrl(url: string): boolean {
  let extension = url.split('.').slice(-1)[0];
  extension = extension.toLowerCase()
  return (extension === 'bmp' || 
      extension === 'jpg' ||
      extension === 'png')
}

export function convertResultToRow(result: Result): string[] {
  const title = result['stitle']
  const region = parseRegionFromAddress(result['address'])
  const longitude = result['longitude']
  const latitude = result['latitude']
  const files = parseFileToFiles(result['file'])
  const imgUrls = files.filter(file => checkImgUrl(file))
  return [title, region, longitude, latitude, imgUrls[0]]
}