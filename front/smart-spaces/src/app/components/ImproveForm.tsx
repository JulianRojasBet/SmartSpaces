"use client";

import { ChangeEvent, useState } from "react";
import { Button } from "@/components/Button";
import { Input } from "@/components/Input";

export function ImproveForm() {
  const [postUrl, setPostUrl] = useState('');

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { value } = event.target
    setPostUrl(value)
  }

  const handleImprove = () => {
    // TODO: Go to next page and fetch data
  }

  return (
    <div className="w-full flex flex-row justify-center py-4 px-4 bg-white rounded-lg shadow-2xl shadow-black">
      <Input value={postUrl} onChange={handleChange} />
      <Button onClick={handleImprove}>Improve</Button>
    </div>
  );
}
