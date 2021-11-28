/// <reference types = "node"/>
declare module "youtube-random-video" {
    export function getRandomVid(key: string | undefined, callback: (error: any | null, data: any | null) => void): void;
}